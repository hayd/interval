from distutils.core import setup

setup(
    name="interval",
    version="1.0.0",
    description="Interval and IntervalSet Data Types",
    long_description= """
      Unlike the built-in sets, IntervalSets contain sets of Interval objects,
      which describe an interval of continuous values.  These IntervalSets can 
      be used in pretty much the same ways as set objects.""",
    author="Jacob Page",
    author_email="jacob.h.page@gmail.com",
    url="http://members.cox.net/apoco/interval/",
    py_modules=["interval"],
    license="LGPL",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Mathematics"])

