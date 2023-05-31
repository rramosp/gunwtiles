from setuptools import setup

setup(name='gunwtiles',
      description="create tiles from JPL Aria GUNW",
      long_description_content_type='text/markdown',
      install_requires=['matplotlib','numpy', 'pandas','joblib',
                        'progressbar2', 'psutil', 'scipy', 'shapely',
                        'geopandas', 'pyproj', 'rasterio', 'retry', 
                        'earthengine-api', 'alphashape', 'rlxutils',
                        'xarray', 'netcdf4'
                       ],
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      scripts=[],
      entry_points={
            "console_scripts": [
                  "gunwt = gunwtiles.main:main",
            ],      
      },
      packages=['gunwtiles'],
      include_package_data=True,
      zip_safe=False)
