from setuptools import setup
import os
from glob import glob

package_name = 'net_bytes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Takeru Harashima',
    maintainer_email='takerujoker936@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = net_bytes.network_info:main',
        'listener = net_bytes.listener:main'
        ],
    },
)    
