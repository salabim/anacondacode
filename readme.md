### <img src="https://www.salabim.org/anacondacode/anacondacode_logo.png" align=left> anacondacode

This module contains one function: `runner`

The function `runner` is intended to be used in Anaconda code cell on an Excel workbook.
It has one parameter: `data`, which can be:

- a reference to an Excel range via the REF function (a list of lists)
- a pandas dataframe
- a numpy array

The data should refer to cells that contain valid Python code. In order to avoid problems, we recommend
to format these cells as text.
The result (if any) of the code should be put in the global `output`.

Each column has uses the same global AnacondaCode namespace. 
But, a column can also be used as were it a module. This is done by placing a

```# module = modulename```

line in the code column.
The given module name then becomes available for ordinary imports in the other code columns.
E.g.

<img src="https://www.salabim.org/anacondacode/anacondacode_poc.png" width=900 align=left>

The global variable `output` can be used to return an accepted value to the sheet (in this case a list of tuples).

You can download the above sheet at: www.salabim.org/anacondacode/anacondacode_poc.xlsx

For more this and more examples, see the samples folder in the anaconda repository (www.github.com/salabim/anacondacode).

#### Installation
Install the module `anacondacode` from PyPI as described in section 'Managing software packages' of https://docs.anaconda.com/excel/code/

#### Disclaimer
This module is in no way affiliated with Anaconda, Inc.

