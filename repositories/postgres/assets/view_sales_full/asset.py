from dagster import asset, Output, AssetIn, MetadataValue
import pathlib


@asset(
    required_resource_keys={'postgres'},
    name='view_sales_full',
    compute_kind='postgres',
    non_argument_deps={
        'products':  AssetIn(key='products'),
        'costumers': AssetIn(key='costumers'),
        'employees': AssetIn(key='employees'), 
        'sales':     AssetIn(key='sales'),
    }
)
def view_sales_full_asset(context):
    ''' Asset for view "view_sales_full" in the Postgres Database. '''

    with open(f'{pathlib.Path(__file__).parent}/sql/ddl.sql', 'r') as file:
        ddl = file.read()

    context.log.info('Droping view "view_sales_full".')
    context.resources.postgres.execute('DROP VIEW IF EXISTS view_sales_full CASCADE')

    context.log.info(f'Creating view "view_sales_full".')
    context.resources.postgres.execute(ddl)

    return Output(
        None,
        metadata={
            'DDL': MetadataValue.md(f'```\n{ddl}\n```')
        }
    )
