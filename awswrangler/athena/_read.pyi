from typing import Any, Dict, Iterator, List, Literal, Optional, Union, overload

import boto3
import pandas as pd

from awswrangler import typing
from awswrangler.athena._utils import _QueryMetadata

@overload
def get_query_results(
    query_execution_id: str,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Union[None, Literal[False]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> pd.DataFrame: ...
@overload
def get_query_results(
    query_execution_id: str,
    *,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Literal[True],
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def get_query_results(
    query_execution_id: str,
    *,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: bool,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
@overload
def get_query_results(
    query_execution_id: str,
    *,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: int,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_query(  # pylint: disable=too-many-arguments
    sql: str,
    database: str,
    ctas_approach: bool = ...,
    unload_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Union[None, Literal[False]] = ...,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    athena_query_wait_polling_delay: float = ...,
    params: Optional[Dict[str, Any]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> pd.DataFrame: ...
@overload
def read_sql_query(
    sql: str,
    database: str,
    *,
    ctas_approach: bool = ...,
    unload_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Literal[True],
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    athena_query_wait_polling_delay: float = ...,
    params: Optional[Dict[str, Any]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_query(
    sql: str,
    database: str,
    *,
    ctas_approach: bool = ...,
    unload_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: bool,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    athena_query_wait_polling_delay: float = ...,
    params: Optional[Dict[str, Any]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
@overload
def read_sql_query(
    sql: str,
    database: str,
    *,
    ctas_approach: bool = ...,
    unload_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: int,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    athena_query_wait_polling_delay: float = ...,
    params: Optional[Dict[str, Any]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_query(
    sql: str,
    database: str,
    *,
    ctas_approach: bool = ...,
    unload_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Optional[Union[int, bool]],
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    athena_query_wait_polling_delay: float = ...,
    params: Optional[Dict[str, Any]] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
@overload
def read_sql_table(
    table: str,
    database: str,
    *,
    unload_approach: bool = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    ctas_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Union[None, Literal[False]] = ...,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> pd.DataFrame: ...
@overload
def read_sql_table(
    table: str,
    database: str,
    *,
    unload_approach: bool = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    ctas_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Literal[True],
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_table(
    table: str,
    database: str,
    *,
    unload_approach: bool = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    ctas_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: bool,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
@overload
def read_sql_table(
    table: str,
    database: str,
    *,
    unload_approach: bool = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    ctas_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: int,
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_table(
    table: str,
    database: str,
    *,
    unload_approach: bool = ...,
    unload_parameters: Optional[typing.AthenaUNLOADSettings] = ...,
    ctas_approach: bool = ...,
    ctas_parameters: Optional[typing.AthenaCTASSettings] = ...,
    categories: Optional[List[str]] = ...,
    chunksize: Optional[Union[int, bool]],
    s3_output: Optional[str] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    keep_files: bool = ...,
    use_threads: Union[bool, int] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    athena_cache_settings: Optional[typing.AthenaCacheSettings] = ...,
    data_source: Optional[str] = ...,
    s3_additional_kwargs: Optional[Dict[str, Any]] = ...,
    pyarrow_additional_kwargs: Optional[Dict[str, Any]] = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
def unload(
    sql: str,
    path: str,
    database: str,
    file_format: str = ...,
    compression: Optional[str] = ...,
    field_delimiter: Optional[str] = ...,
    partitioned_by: Optional[List[str]] = ...,
    workgroup: Optional[str] = ...,
    encryption: Optional[str] = ...,
    kms_key: Optional[str] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    data_source: Optional[str] = ...,
    params: Optional[Dict[str, Any]] = ...,
    athena_query_wait_polling_delay: float = ...,
) -> _QueryMetadata: ...
