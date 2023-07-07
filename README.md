# Ex-to-Lanraragi

## What is Ex-to-Lanraragi?
Ex-to-Lanraragi is a set of tools for downloading galleries from ex-hentai and preparing them with their metadata for Lanraragi.
  ### Basic Usage
    1. Download a gallery from Ex-Hentai
    2. Run mayoi-mover.py

  These two actions will download an Ex-Hentai gallery and prepare its archive with the relevant metadata(in the format of chaika.moe metadata). Note, these downloads will require hath.

## Requirements

- Python 3
  - python requests module
- Web server with php5+
- Google Chrome

## Installation and configuration

Extract the following files/folders to somewhere on your webserver.
- Downloads (folder)
- archive.php
- panda.php

Note the path of archive.php as we will need this later.

Extract the chrome-addin folder to anywhere on your local computer.

## Configuring web files
Open panda.php in the text editor of your choice.

#### panda.php
  - Edit lines 21 and 22 to contain your ipb_pass_hash and ipb_member_id cookies.
    - To find these values, navigate to Ex-Hentai and open chrome developer tools(F12).
    - With developer tools, navigate to the network tab and refresh the page. Once the page is refreshed, press ctrl+f within developer tools and search for "ipb_". You will see the value of the cookies.
  - Edit lines 24 and 25 depending on the quality of download you want.

## Configuring Chrome addin
Within the chrome-addin folder open manifest.json and eventPage.js with the text editor of your choice.

#### manifest.json
  - Edit line 21 "http://YOURURLTOSERVERHERE" to be the root of your webserver.

#### eventPage.js
  - Edit line 16 "fetch("http:YOURURLTOSERVER/archive.php?galID="+gid+"&galToken="+gtkn)" to contain the path to your archive.php

## Configuring Mayoi-Mover
  Open Downloads/mayoi-mover.py in the text editor of your choice.

  - Edit line 73 to be the path of your Lanraragi galleries folder or any other folder you want finished galleries to be placed in.

## Configuring Lanraragi
In Lanraragi configure the following settings
  - Settings > Plugin Configuration > Metadata Plugins > Chaika.moe api.json > Set to Run Automatically

You are ready to start downloading! To download a gallery on Ex-Hentai, simply right click its preview and click "Add Gallery to Lanraragi". Alternatively, you can right click anywhere on the galleries info page and click the same button.
