from dagster import repository, build_asset_reconciliation_sensor, AssetSelection
from repositories import *


assets_reconciliation_sensor = build_asset_reconciliation_sensor(
    asset_selection=AssetSelection.all(),
    name='assets_reconciliation_sensor'
)


@repository
def postgres():
    '''  This repository is responsible for all jobs and assets related to Postgres. '''

    return [
        postgres_assets,
        assets_reconciliation_sensor
    ]
