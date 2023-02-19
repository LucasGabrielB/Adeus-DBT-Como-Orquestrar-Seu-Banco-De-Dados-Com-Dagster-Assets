from dagster import asset, Output, MetadataValue, AssetIn
import pathlib


@asset(
    required_resource_keys={'postgres'},
    name='sales',
    compute_kind='postgres',
    non_argument_deps={
        'products':  AssetIn(key='products'),
        'costumers': AssetIn(key='costumers'),
        'employees': AssetIn(key='employees'), 
    }
)
def sales_asset(context):
    ''' Asset for table "sales" in the Postgres Database. '''

    with open(f'{pathlib.Path(__file__).parent}/sql/ddl.sql', 'r') as file:
        ddl = file.read()

    context.log.info(f'Creating table "sales".')
    context.resources.postgres.execute(ddl)

    return Output(
        None,
        metadata={
            'DDL': MetadataValue.md(f'```\n{ddl}\n```')
        }
    )
