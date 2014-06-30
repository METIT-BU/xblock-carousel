xblock-carousel
=============
Xblock to provide carousel of multimedia instructional content including images, video, documents.
This xBlock currently supports three web hosted media formats in a unified media carousel for course content presentation. This Xblock also provides a way to integrate instructional media with a separate workspace that could be used for hands-on activities.

* **Images**- Any web hosted image in a format supported by the HTML <img> tag (jpg, png, gif) 
* **Youtube Videos**- Any YouTube hosted video.
* **Documents**- Web hosted documents are rendered though Google Doc Viewer and can in and supported format. (pdf, doc, xls, ppt)

A demo for the above xblock can be found [here](http://met-testedx2.bu.edu:8000/courses/MET/101/2014/about "Carousel XBlock demo")

* **user**: user@test.com
* **password**: user

Examples
--------
### Images, Videos and Documents
```xml
<carousel>
  <img src="http://met-content.bu.edu/etr2/content/images/Slide1.JPG" />
  <img src="http://met-content.bu.edu/etr2/content/images/Slide2.JPG" />
  <img src="http://met-content.bu.edu/etr2/content/images/Slide3.JPG" />
  <video src="http://www.youtube.com/watch?v=7uHeNryKUWk" />
  <doc src="http://www.bu.edu/met-eti/files/2013/03/Final_VirtualLaboratoriesForLearning.pdf" />
</carousel>
```

TO-DO: 
------

* Add support for mp4 webm videos, other providers
* Add support for html tags
* Add support for the documents uploaded to the studio static folder
* Add support for mozilla-pdf.js
* Replace xml etree with lxml 
