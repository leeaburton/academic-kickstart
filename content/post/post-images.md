+++
title = "Post: Images"
date = 2018-02-19T14:35:20+01:00
draft = false

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = []
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
# Use `caption` to display an image caption.
#   Markdown linking is allowed, e.g. `caption = "[Image credit](http://example.org)"`.
# Set `preview` to `false` to disable the thumbnail in listings.
[header]
image = ""
caption = ""
preview = true

+++

There are many many ways for scientists to make 3D images. I'm going to focus on just 2 software packages called <a href="http://jp-minerals.org/vesta/en/">VESTA</a> and <a href="https://www.blender.org/">Blender</a>. Vesta is my go-to visualisation tool, I've used it since day one and it's very intuitive and flexible. Blender on the other hand is a more involved and complicated process but this software offers the possibility for professional grade 3D images and even CGI animations. Oh and they're both free! :)

Right, to begin with you have to load a specific addon called <a href="https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/PDB">Atomic Blender</a>, so that blender will understand chemical structures.

After opening Blender, click File -> User preferences, then the Add-ons tab. Here you have to tick "Import-Export: Atomic Blender - PDB".

From now on you can load "protein data bank (pdf) files" into blender (it seems like recently you can also load XYZ files with atomic blender but I'll need to check that).  Vesta allows you to export pdb files by default, so now there is a pathway to load structures into professional 3D imaging software without having to modify anything by hand.

TODO: I just realised I need to look in to public licences and permission before i start posting images and explanations to this. I guess that's going to be another post in itself!
