# Panopto Sessions Database

Analyzizing Panopto sessions so we can create scenarios for our retention policy.

Questions:

- how many sessions have never been watched?
  - what sorts of folders are those sessions in?
  - what is their **Stream Source**?
- how many sessions haven't been watched _in the last year_?

https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html

`csvjoin -c 2 --outer sessionscreatedoredited_2020-08-08--2022-06-01.csv sessionusage_2020-08-08--2022-06-01.csv > sessions.csv`

```sh
> head -n1 sessionusage_2020-08-08--2022-06-01.csv
Session Name,Session ID,Creator,Creator ID,Email,Start Time,Folder Name,Folder ID,Views and Downloads,Unique Viewers,Minutes Delivered,Average Minutes Delivered,Session Length,Rating Count,Average Rating,Most Recent View Date,Root Folder (Level 0),Subfolder (Level 1),Subfolder (Level 2),Subfolder (Level 3),Subfolder (Level 4)
> head -n1 sessionscreatedoredited_2020-08-08--2022-06-01.csv
Session Name,Session ID,Creator,Creator ID,Email,Folder Name,Folder ID,Start Time,Last Time Edited,Last Approval Action,Last Approval Time,Last Approver Name,Last Approver Id,Session Length,Stream Count,Stream Source,Rating Count,Average Rating,Root Folder (Level 0),Subfolder (Level 1),Subfolder (Level 2),Subfolder (Level 3),Subfolder (Level 4)
# insert CSV data into sqlite database
> csvsql --tables sessions --db sqlite:///pano.db --insert --overwrite sessionscreatedoredited_2020-08-08--2022-06-01.csv
> csvsql --tables usage --db sqlite:///pano.db --insert --overwrite sessionusage_2020-08-08--2022-06-01.csv
> sqlite pano.db
```
