from dagster import asset, Output, MetadataValue
import pathlib


@asset(
    required_resource_keys={'postgres'},
    name='employees',
    compute_kind='postgres',
)
def employees_asset(context):
    ''' Asset for table "employees" in the Postgres Database. '''

    with open(f'{pathlib.Path(__file__).parent}/sql/ddl.sql', 'r') as file:
        ddl = file.read()

    context.log.info(f'Creating table "employees".')
    context.resources.postgres.execute(ddl)

    return Output(
        None,
        metadata={
            'DDL': MetadataValue.md(f'```\n{ddl}\n```')
        }
    )
