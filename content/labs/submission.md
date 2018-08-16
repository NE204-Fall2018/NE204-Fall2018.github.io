title: Lab Submissions
article-order: 02
date: 2018-08-16

Each report will be built from the source files (LaTeX and any figures in the
`images/` directory, for example).
To make this simpler, the lab report template comes with a `Makefile`.
Using the GNU `make` utility, a .pdf of the lab report is compiled from the 
LaTeX source files by typing `make`.
Note that, even if you submit a .pdf in the git repo for your report, it will 
be ignored!
The report that will be evaluated is the one that is generated using the 
`Makefile`.

There are several other commands in the `Makefile`, two of which *must* be
implemented to obtain full credit for the submitted report (see the
[rubric]({filename}/labs/rubric.md) for details).

 1. `make test`: You must implement some rudimentary unit-tests for your code.

 2. `make data`: You must implement a method for downloading any data relevant
    for your analysis.

If you have no idea what this means, don't worry.
It will be covered in our first lab session(s), and the in-class
example detailing these features will thereafter be available on 
[the course github page](https://github.com/NE204-Fall2018).

It is not *required* that students use the 
[provided template](https://github.com/NE204-Fall2018/lab_report_template) to
strucure their lab reports.
For example, if you do not want to use make, you can replace the `Makefile` 
with a build script of your own design.
However, if you choose to do so, the README for your project must include the
following information:
 
 1. Instructions for building your report from the source files
 2. Instructions for running your code tests
 3. Instructions for downloading any relevant data

Note that these "Instructions" should be in the form of a script(s) that can be
run on the command line.

### Validating your submission

The best way to verify that your report is going to come out the way you 
expect it to is to clone a fresh version of your report repository and build
it from scratch.

### Submitting via Github

All lab reports will be submitted via github.
To submit your lab report, use the following procedure:

 1. Go to the class [Github organization](https://github.com/orgs/NE204-Fall2018/dashboard).
 2. Click the button to create a new repository.
 3. Name the repository <your\_github\_username\>-lab<\#\>. For example, if
    I were creating a repository to submit lab 4, the repository would be named
    **rossbar-lab4**.
 4. Add the link to the remote repository you just created to your list of
    remotes in your local repository.
    Again taking my submission of lab 4 as an example:
    `git remote add submission https://github.com/NE204-Fall2018/rossbar-lab4.git`
 5. Push your local repository to the newly created remote named "submission":
    `git push submission master`.

Whatever is on the master branch of this repository at 9PM on the due date
will be considered your submission.
