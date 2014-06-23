xblock-carousel
=============
Xblock to provide carousel of multimedia content including images, video, documents(pdf, ppt, doc, etc...).
This xBlock supports three wed hosted media formats in a unified media carousel for course content presentation.

* **Images**- Any web hosted image in a format supported by the HTML <img> tag (jpg, png, gif) 
* **Youtube Videos**- Any YouTube hosted video.
* **Documents**- Web hosted documents are rendered though Google Doc Viewer and can in and supported format. (pdf, doc, xls, ppt)

A demo for the above xblock can be found [here](http://met-testedx2.bu.edu:8000 "Carousel XBlock demo")

Examples
--------
### Images, Videos and Documents
```xml
<carousel>
  <img>http://met-content.bu.edu/etr2/content/images/Slide1.JPG</img>
  <img>http://met-content.bu.edu/etr2/content/images/Slide2.JPG</img>
  <img>http://met-content.bu.edu/etr2/content/images/Slide3.JPG</img>
  <video>http://www.youtube.com/watch?v=7uHeNryKUWk</video>
  <doc>http://www.bu.edu/met-eti/files/2013/03/Final_VirtualLaboratoriesForLearning.pdf</doc>
</carousel>
```

TO-DO: 
------

* Add support for mp4 webm videos, other providers
* Add support for html tags
* Add support for the docuents uploaded to the studio static folder
* Add support for mozilla-pdf.js
* Replace xml etree with lxml 
