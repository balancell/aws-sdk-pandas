"""Ray and Modin registered methods (PRIVATE)."""
# pylint: disable=import-outside-toplevel
from awswrangler._data_types import pyarrow_types_from_pandas
from awswrangler._distributed import MemoryFormatEnum, engine, memory_format
from awswrangler._executor import _get_executor
from awswrangler._utils import (
    copy_df_shallow,
    ensure_worker_or_thread_count,
    is_pandas_frame,
    split_pandas_frame,
    table_refs_to_df,
)
from awswrangler.distributed.ray import ray_remote
from awswrangler.distributed.ray._executor import _get_ray_executor
from awswrangler.distributed.ray._utils import ensure_worker_count
from awswrangler.distributed.ray.s3._list import _list_objects_s3fs
from awswrangler.distributed.ray.s3._read_parquet import _read_parquet_metadata_file_distributed
from awswrangler.dynamodb._read import _read_scan
from awswrangler.dynamodb._write import _put_df, _put_items
from awswrangler.lakeformation._read import _get_work_unit_results
from awswrangler.s3._copy import _copy_objects
from awswrangler.s3._delete import _delete_objects
from awswrangler.s3._describe import _describe_object
from awswrangler.s3._list import _list_objects_paginate
from awswrangler.s3._read_parquet import _read_parquet, _read_parquet_metadata_file
from awswrangler.s3._read_text import _read_text
from awswrangler.s3._select import _select_object_content, _select_query
from awswrangler.s3._wait import _wait_object_batch
from awswrangler.s3._write_dataset import _to_buckets, _to_partitions
from awswrangler.s3._write_parquet import _to_parquet
from awswrangler.s3._write_text import _to_text
from awswrangler.timestream._write import _write_batch, _write_df


def register_ray() -> None:
    """Register dispatched Ray and Modin (on Ray) methods."""
    for func in [
        _get_work_unit_results,
        _copy_objects,
        _describe_object,
        _delete_objects,
        _read_scan,
        _select_query,
        _select_object_content,
        _wait_object_batch,
    ]:
        # Schedule for maximum concurrency
        engine.register_func(func, ray_remote(scheduling_strategy="SPREAD")(func))

    for func in [
        _put_df,
        _put_items,
        _write_batch,
        _write_df,
    ]:
        engine.register_func(func, ray_remote()(func))

    for o_f, d_f in {
        _get_executor: _get_ray_executor,
        _list_objects_paginate: _list_objects_s3fs,
        _read_parquet_metadata_file: ray_remote()(_read_parquet_metadata_file_distributed),
        ensure_worker_or_thread_count: ensure_worker_count,
    }.items():
        engine.register_func(o_f, d_f)  # type: ignore[arg-type]

    if memory_format.get() == MemoryFormatEnum.MODIN:
        from awswrangler.distributed.ray.modin._data_types import pyarrow_types_from_pandas_distributed
        from awswrangler.distributed.ray.modin._utils import (
            _arrow_refs_to_df,
            _copy_modin_df_shallow,
            _is_pandas_or_modin_frame,
            _split_modin_frame,
        )
        from awswrangler.distributed.ray.modin.s3._read_parquet import _read_parquet_distributed
        from awswrangler.distributed.ray.modin.s3._read_text import _read_text_distributed
        from awswrangler.distributed.ray.modin.s3._write_dataset import (
            _to_buckets_distributed,
            _to_partitions_distributed,
        )
        from awswrangler.distributed.ray.modin.s3._write_parquet import _to_parquet_distributed
        from awswrangler.distributed.ray.modin.s3._write_text import _to_text_distributed

        for o_f, d_f in {
            pyarrow_types_from_pandas: pyarrow_types_from_pandas_distributed,
            _read_parquet: _read_parquet_distributed,
            _read_text: _read_text_distributed,
            _to_buckets: _to_buckets_distributed,
            _to_parquet: _to_parquet_distributed,
            _to_partitions: _to_partitions_distributed,
            _to_text: _to_text_distributed,
            copy_df_shallow: _copy_modin_df_shallow,
            is_pandas_frame: _is_pandas_or_modin_frame,
            split_pandas_frame: _split_modin_frame,
            table_refs_to_df: _arrow_refs_to_df,
        }.items():
            engine.register_func(o_f, d_f)  # type: ignore[arg-type]
