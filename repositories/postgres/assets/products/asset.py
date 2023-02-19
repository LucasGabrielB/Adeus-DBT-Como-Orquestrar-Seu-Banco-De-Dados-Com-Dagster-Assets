from dagster import asset, Output, MetadataValue
import pathlib


@asset(
    required_resource_keys={'postgres'},
    name='products',
    compute_kind='postgres',
)
def products_asset(context):
    ''' Asset for table "products" in the Postgres Database. '''

    with open(f'{pathlib.Path(__file__).parent}/sql/ddl.sql', 'r') as file:
        ddl = file.read()

    context.log.info(f'Creating table "products".')
    context.resources.postgres.execute(ddl)

    return Output(
        None,
        metadata={
            'DDL': MetadataValue.md(f'```\n{ddl}\n```')
        }
    )
