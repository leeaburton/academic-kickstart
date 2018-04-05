+++
title = "Project: Light"
date = 2018-02-19T14:58:40+01:00
draft = false

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = []

# Project summary to display on homepage.
summary = "Average light intensity by latitude and longitude."

# Optional image to display on homepage.
image_preview = ""

# Optional external URL for project (replaces project detail page).
external_link = ""

# Does the project detail page use math formatting?
math = false

# Does the project detail page use source code highlighting?
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This is another side-project based on data from NASA. I found the information for amount of sunlight at each point on the planet for latitude and longitude. I cross referenced this with the coordinates for cities in the world to see which is the sunniest place.

I tried to factor in electricity cost and use that to find the best location in the world to put solar panels in terms of profit return, rather than for example some amazing work been done in Africa on an almost charity basis. A combination of expensive electricity and intense sunlight was the most desirable.

One problem is the available data for electricity cost is really hard to come by in a consistent way. Another problem I found when I pitched this idea to a mock panel of investors, is that political instability is a huge problem for something like this. The top 2 or 3 locations returned by my code were in relatively volatile parts of the world and the panel were not keen. Needless to say I did not win that competition :p

Now my plan is a little different. In Project: World I'm developing the data for world land area. This can then be overlayed with the data I have here for available sunlight to create an estimate of global solar energy potential. This is just one straight-forward idea. I'm hoping that by putting these resources side by side on this sight I can form separate but complimentary projects to build towards something.

TO DO: make a plot of the solar intensity data as a grid. 
TO DO: tidy up the script and put it on github linked here.

 
