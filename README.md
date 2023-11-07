# Alfred Org Boookmarks

This workflow allows you to manage your bookmarks independent from your browser in an org file and access them quickly through alfred.

## Setup

1. Install the workflow
2. Set the location of your bookmarks file
3. Put your bookmarks into the org file
4. Have fun...

## File format
Bookmarks are stored as links in dedicated nodes in the org file.
All higher order nodes will be used to construct the title. This way you can organize your bookmarks in sections.

**Example:**

``` org
* Work
** [[https://mycompany.com][My company]]
** [[https://duckduckgo.com][Duck Duck Go]]

* Hobbies
** Canoeing 
*** [[https://lettmann.com][Lettmann Canoes]]
** Base Jumping
*** [[https://iwoouldneverdothis.com][Base Jumping]]
```

This would end up in the following list in Alfred:

* Work/My company
* Work/Duck Duck go
* Hobbies/Canoeing/Lettmann Canoes
* Hobbies/Base Jumping/Base Jumpin
