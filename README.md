# Fibonacci Calculation

This repo is related to the **Algorithm All-Hands Projects** (AAHP) described within the [Algorithmology.org](https://algorithmology.org/) curriculum.

This is the second AAHP within the Spring 2025 cohort of Algorithmology at [Allegheny College](https://sites.allegheny.edu/computer-science/) (CMPSC 202-00) taught by [Dr. Gregory M Kapfhammer](https://github.com/gkapfham).

The findings from this project can be found on the Algorithmology.org website, here: [algorithmology.org/allhands/spring2025/weekeleven/teamthree/](https://algorithmology.org/allhands/spring2025/weekeleven/teamthree/).

## Algorithm All-Hands Projects

These projects enable students to explore both the scientific and engineering aspects of algorithm analysis, as outlined in the course schedule. During the completion of a scientific study phase of algorithm analysis, students will work in a team to propose an original research question and design an experiment to answer it. When completing an engineering effort phase of algorithm analysis, students work in a team as they design, implement, document, test, and maintain software tools that support the rigorous evaluation of the performance (e.g., time or space overhead) of a Python program. The conclusion of an algorithm all-hands project involves the team-based creation, publication, and oral presentation of a report that overviews all of the experiences during the completion of the scientific study and engineering effort tasks for answering an original research question in the field of algorithm analysis. Students may use external sources, including artificial intelligence coding assistants, during the completion of an algorithm all-hands project provided that they cite these sources and explain how they used them to complete their part(s) of an algorithm all-hands project.

## Team

The group working on the project housed in this repo is:

* [Duru Akbas](https://github.com/duruakbas)
* [Faaris Cheema](https://github.com/Faarisc)
* [Hank Gref](https://github.com/hankgref)
* [Kris Hatcher](https://github.com/krishatcher)
* [Titus Smith](https://github.com/TitusSmith33)

## Project Description

### Research Question

What is the fastest method to build a Fibonacci sequence when considering recursive, iterative, and memoized approaches?

### Evaluation Metrics

TODO: document evaluation metrics once decided upon

### Process

* Each member of the team was assigned a portion of the code implementation to complete.
* Once all code is implemented, each team member will run the same set of benchmarking runs and add their data to the shared Google Sheet.
* Each team member will then complete part of a writeup, specifically a portion of the writeup about the code they implemented. This writeup will be published on [algorithmology.org/allhands](https://algorithmology.org/allhands/) at the conclusion of the project.

The set of runs each team member completed are listed below. This same set of commands is included as a shell file (`benchmark_commands.sh`) which can be run as a simpler way to get the same output.

| ID  | Quantity | Approach    | Runs | Repeats |
| :-: | :------: | ----------- | :--: | :-----: |
| 1   | 7        | iterative   | 15   | 5       |
| 2   | 14       | iterative   | 15   | 5       |
| 3   | 28       | iterative   | 15   | 5       |
| 4   | 7        | recursive   | 15   | 5       |
| 5   | 14       | recursive   | 15   | 5       |
| 6   | 28       | recursive   | 15   | 5       |
| 7   | 7        | memoization | 15   | 5       |
| 8   | 14       | memoization | 15   | 5       |
| 9   | 28       | memoization | 15   | 5       |

## Running the Experiment

In order to execute the code in this repo, a user must call the CLI function and pass in options.

### Command Options

To run the program, the minimum required is to simply enter `poetry run fibonacci` in the command line, while in the context of `/fibonacci` within this repo's structure. All options have default values (described below) that will be used to run the tool. The commands below would be added to that base command.

* Quantity
  * Default Value: `100`
  * Accepted Values: integers
  * The number of entries in the Fibonacci sequence to be calculated within each benchmark run.
* Approach
  * Default Value: `iterative`
  * Accepted Values: `iterative`, `recursive`, and `memoization`
  * Which algorithm should be utilized to calculate the Fibonacci sequence.
* Runs
  * Default Value: `15`
  * Accepted Values: integers
  * How many runs should be performed within each set of benchmarking operations.
* Repeats
  * Default Value: `5`
  * Accepted Values: integers
  * How many sets of benchmarking operations should be performed.

### Output

Here is sample output from the three different approaches, for reference.

```command
> poetry run fibonacci --quantity 30 --approach recursive                    
===========================================================================
                           Fibonacci Calculation                           
===========================================================================
 Calculating the first 30 entries in the Fibonacci sequence.
 Performing 5 sets of 15 runs of the 'recursive' calculation approach.
---------------------------------------------------------------------------
 Total time (sec) for each set of runs:
[
    2.5239038089930546,
    2.4771195789944613,
    2.478744343010476,
    2.535703239002032,
    2.4424135130102513
]

 Average times (sec) for each set of runs:
[0.504781, 0.495424, 0.495749, 0.507141, 0.488483]
===========================================================================
> poetry run fibonacci --quantity 30 --approach iterative
===========================================================================
                           Fibonacci Calculation                           
===========================================================================
 Calculating the first 30 entries in the Fibonacci sequence.
 Performing 5 sets of 15 runs of the 'iterative' calculation approach.
---------------------------------------------------------------------------
 Total time (sec) for each set of runs:
[
    1.7589001799933612e-05,
    1.4267992810346186e-05,
    1.4136996469460428e-05,
    1.4004006516188383e-05,
    1.370999962091446e-05
]

 Average times (sec) for each set of runs:
[4e-06, 3e-06, 3e-06, 3e-06, 3e-06]
===========================================================================
> poetry run fibonacci --quantity 30 --approach memoization
===========================================================================
                           Fibonacci Calculation                           
===========================================================================
 Calculating the first 30 entries in the Fibonacci sequence.
 Performing 5 sets of 15 runs of the 'memoization' calculation approach.
---------------------------------------------------------------------------
 Total time (sec) for each set of runs:
[
    0.000105518993223086,
    9.980199683923274e-05,
    9.930200758390129e-05,
    9.91460110526532e-05,
    9.923099423758686e-05
]

 Average times (sec) for each set of runs:
[2.1e-05, 2e-05, 2e-05, 2e-05, 2e-05]
===========================================================================
```
