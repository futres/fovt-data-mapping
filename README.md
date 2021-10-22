# data mapping of legacy data to the template

For some users we've written custom scripts, but we prefer if users input data using the template in <a href="https://geome-db.org/workbench/template"> GEOME</a>.

Users can also use the <a href="">R Shiny App</a> designed to help transform short-form data to long-form data (i.e., one trait record per row).

We work with the data contributer to make sure the terms map correctly to the terms already in the <a href="http://obofoundry.org/ontology/fovt">FOVT</a>. Data mapping and clean up are doing using Jupyter notebook in /scripts.

1. Data mapping files use data imported into the <a href="de.cyverse.org">Discovery Environment</a>.
2. Mapped files are then uploaded as a project and validated in <a href="https://geome-db.org/workbench/template"> GEOME</a>. 
3. These projects, which are part of the FuTRES Team Project, then run through the <a href="">FuTRES pipeline</a>.

To request terms, please see the <a href="github.com/futres/fovt">FOVT GitHub</a> and submit an issue.

## R Shiny App

We are creating the following functions to help researchers clean and standardize their data to be uploaded to GEOME

1. standardizing sex terms to "male" or "female"
2. standardizing element side to "right" or "left"
3. mapping column names to those found in the <a href="https://geome-db.org/workbench/template">template</a>
4. mapping measurementType to ontology terms 
5. creating UUIDs for the individual organism (individualID), element from the individual of interest (materialSampleID), and measurement (diagnosticID)
6. standardizing lifeSatge as "adult" or "juvenile"
7. standardizing reproductive condition to "non-reproductive" or "reproductive"
