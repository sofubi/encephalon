LATER:
- [ ] Create basic logging for error reporting
- [ ] Add progress to logging
- [ ] Decide on how to manage scheduling
    - [ ] Include the basics as part of tool
    - [ ] What are common schedulers to consider
- [ ] Ways to clean up notes
    - [ ] Strip linebreaks, newlines, etc.
    - [ ] Any other needs?
- [ ] Extensible and customizable file management
    - [ ] Once ingested, move notes to a structure chosen by users
    - [ ] How should users dictate file management?
    - [ ] What should default strategy be?
- [ ] Customizable regex markers
    - [ ] Make the capture dynamic to user input
- [ ] Customizable and dynamic template metada
    - [ ] Templates that are recognized by tokens within notes
    - [ ] Automatic frontmatter
    - [ ] Dynamic pieces of frontmatter (date, time)

TODO:
- [ ] Begin working on managing files/folders and distributing notes after ingestion
- [ ] Continue writing tests

MVP:
- [x] Ingests notes files
- [ ] Manages folder and file structure
- [ ] Has basic scheduling
- [ ] Has user schedulability with 3rd party services (systemd, cron, etc.)


THOUGHTS:
- ~~Files may be large -> how should a large file be handled?~~
- Each file may have many notes -> how should notes be held intermediately?
  - Pass off each match to a tmp file then flush?
- Think about being passed more than one file path - n number of note files


How can I save a notes file with multiple notes that is reparseable?
Should each "note" be discrete within a folder?
I need a way to append to notes files.

NEED A CLASS FOR:
- Notes
- Folders

Need parser that parses notes conent and finds (substring search):
- folder structure within top level (if no structure store in top level)
- format to save note in (default to .md)