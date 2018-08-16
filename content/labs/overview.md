title: Lab Overview
article-order: 01
date: 2018-08-16

The primary objective of this course is to provide students with hands-on
experience with advanced concepts in radiation detection and measurement.
In particular, the laboratory portion emphasizes:

 - Digital signal processing
 - Signal generation & pulse shape analysis
 - Multichannel detector systems
 - Radiation imaging

Ideally, we'd like for all students to have an opportunity to investigate all 
of these concepts (and more) with each of the state-of-the-art radiation
instruments we have available.
Unfortunately, given the complexity of many of the experiments; the limited
instrument availability relative to the number of students; and realistic time 
constraints; it is simply not possible for each student to be able to conduct
every proposed experiment to a satisfactory degree.
Instead, students will be expected to focus on three predefined laboratory 
experiments, and propose a fourth to be studied in greater detail for the
final project.
The first two labs deal with digital signal processing and will be 
investigated by each lab group.
A third lab on multichannel detector systems is planned, but which exact 
investigation will be done will depend on individual groups and equipment
availability.
Ultimately, the total number of labs to be done is subject to change, with the
goal of allowing students to conduct as many as possible, while maximizing
the time students spend on topics they are personally interested in.

## List of Labs

Links to the lab writeups will be made available over the course of the
semester.

  1. Digital Signal Processing in HPGe - Spectroscopy
  2. Digital Signal Processing in HPGe - Pulse Shape and Timing
  3. Digital Signal Processing in LaBr - Spectroscopy & Timing
  4. Neutron Detection and Pulse Shape Discrimination in Liquid Scintillation
     Detectors
  5. Position Determination in Segmented HPGe
  6. Position Determination in Pixelated CZT
  7. Charge Transport Properties in Segmented HPGe
  8. Charge Transport Properties in Pixelated CZT
  9. Gamma-Ray Imaging with Segmented HPGe
  10. Neutron Imaging with Liquid Scintillator Array

## Reproducibility and Scientific Computing

Another important objective of this course is to give students practical
experience conducting scientific research with a reproducible workflow.
Reproducibility is a foundational component of scientific investigatiion.
Without the ability to effectively communicate technical ideas and test and
replicate proposed experiments, the scientific enterprise would not
be possible.
On a more practical note, reproducibility is also a key component in 
collaborative efforts.
A ubiquitous and utterly demoralizing experience for graduate students in STEM
fields is dealing with "legacy" systems and codebases, where "things just used
to work".
The amount of effort that has been lost/wasted due to corrupted hard drives,
impenatrable and unmaintainable codebases, or an experienced post doc leaving
for a new job is both staggering and depressing.
Fortunately, these hair-loss-inducing impediments to the expansion of human
knowledge are avoidable, especially now that so much of the scientific 
endeavor takes place in the digital domain.
The primary antidote is the *reproducible* workflow.
Some key components of a reproducible workflow are:

 - Using *accessible* tools for data analysis, so that other people are able to
   test your ideas.
 - Using tools that are *tested* and maintained to minimize errors in results
 - A tight coupling between the *analysis* (e.g. code) and the *presentation of
   the results* (e.g. report).
 - *Version control* to keep track of changes to both the analysis and
   accompanying text/figures for presenting the results.

In this course, students will implement a reproducible workflow for the lab
work using the incredibly powerful
[Python ecosystem for scientific computing](http://www.scipy-lectures.org/intro/intro.html),
along with [Git](https://git-scm.com/book/en/v2) for version control and 
[LaTeX](https://www.latex-project.org/): the de facto standard for generating
technical documents.

**N.B.** For a much more detailed and compelling description of reproducible
workflows (and scientific computation in general), I refer to the seminal 
textbook on the topic: 
[Effective Computation in Physics](http://physics.codes/) by  
[Kathryn Huff](http://katyhuff.github.io/) and 
[Anthony Scopatz](http://www.ergs.sc.edu/people/scopatz.html).

## Lab Report Template

In order to facilitate a "learn-by-doing" approach, a 
[lab report template](https://github.com/NE204-Fall2018/lab_report_template)
is available in the course Github organization.
Instructions for the basic usage of the template can be found in the README.

## Lab Report Submission and Grading

Information about how to structure and submit lab reports can be found in
the [submission instructions]({filename}/labs/submission.md).  

A detailed breakdown of how the lab reports will be evaluated can be found
in the [lab report rubric]({filename}/labs/rubric.md).
