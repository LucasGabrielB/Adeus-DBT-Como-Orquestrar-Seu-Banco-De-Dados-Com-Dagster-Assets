from resources import postgres
from dagster import with_resources
import os

from .costumers       import costumers_asset
from .employees       import employees_asset
from .products        import products_asset
from .sales           import sales_asset
from .view_sales_full import view_sales_full_asset

postgres_assets = with_resources(
    [   
        costumers_asset,
        employees_asset,
        products_asset,
        sales_asset,
        view_sales_full_asset
    ],
    resource_defs={
        'postgres': postgres.postgres_connection,
    },
)
