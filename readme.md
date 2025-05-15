# Panopto Sessions Data

Analyzing Panopto session creation and usage so we can create scenarios for our retention policy.

## Setup

This project uses python3 and [uv](https://docs.astral.sh/uv) for dependency management. Run `uv sync` to create a virtualenv. Then open the iPython notebook (e.g. in Visual Studio Code or iPython's own app) to work on the data. We may need to tell the notebook app where the virtualenv is located.

## Panopto Reports

To get started, go to the Panopto System settings and select [Usage](https://ccarts.hosted.panopto.com/Panopto/Pages/Admin/Usage.aspx#), then **Create new report**. For the reports, select dates that cover our whole subscription (August 8th, 2020 to yesterday). The "Sessions created or edited" report provides information on the length and Stream Source of sessions; the "Session usage" report provides data on how many times a session was watched and when the last time it was watched. If you want the scripts here to work as is, rename the reports to "sessionscreatedoredited.csv" and "sessionusage.csv" respectively.

Other reports could be added. "Session ID" is the key that links together session data from different reports.

## Questions

- How many sessions have never been watched?
  - What is their **Stream Source**?
  - What sorts of folders are those sessions in?
- How many sessions have been watched at least once?
  - What kinds of sessions tend to go watched vs. unwatched?
- How many sessions haven't been watched _in the last year_?
  - Same sub-questions about folders and source

## Non-iPython Notebook approaches

Here are the fields contained in the two sessiosn reports:

```sh
> head -n1 sessionusage.csv
Session Name,Session ID,Creator,Creator ID,Email,Start Time,Folder Name,Folder ID,Views and Downloads,Unique Viewers,Minutes Delivered,Average Minutes Delivered,Session Length,Rating Count,Average Rating,Most Recent View Date,Root Folder (Level 0),Subfolder (Level 1),Subfolder (Level 2),Subfolder (Level 3),Subfolder (Level 4)
> head -n1 sessionscreatedoredited.csv
Session Name,Session ID,Creator,Creator ID,Email,Folder Name,Folder ID,Start Time,Last Time Edited,Last Approval Action,Last Approval Time,Last Approver Name,Last Approver Id,Session Length,Stream Count,Stream Source,Rating Count,Average Rating,Root Folder (Level 0),Subfolder (Level 1),Subfolder (Level 2),Subfolder (Level 3),Subfolder (Level 4)
```

We can join the two reports CSVs together into one spreadsheet:

`csvjoin -c 2 --outer sessionscreatedoredited.csv sessionusage.csv > sessions.csv`

Note that the overlapping columns will be duplicated (and numbered to distinguish themselves), but they can also just be ignored.

We can also create a sqlite database from the reports CSVs using [the `csvsql` command](https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html).

```sh
# insert CSV data into sqlite database
> csvsql --tables sessions --db sqlite:///pano.db --insert --overwrite sessionscreatedoredited.csv
> csvsql --tables usage --db sqlite:///pano.db --insert --overwrite sessionusage.csv
> sqlite pano.db # connect to the db to run queries
```

The insert.py script is a code-based approach to accomplishing the same task. It could be expanded to combine the two tables and drop duplicate columns using the approach at the top of the iPython notebook, for instance.
