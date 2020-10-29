# Hi there 👋

Hey, how is it going? My name is Philipp. Let me tell you something about myself. ✌ I study Computer Science at TU Dresden (on Diploma, currently in the 9th semester). I work at TU Dresden as a developer and tutor since April 2018. Additionally, I am self-employed as a software developer and designer.
I like 🏸 badminton, 🏂 snowboarding, 🚴🏼‍ cycling and 🏋🏻‍ any other kind of sports.

# I learn by creating 💡.

Here is a selection of some projects I worked on, sorted by their topics:
- [Applied Machine Learning and Artificial Intelligence](#applied-machine-learning-and-artificial-intelligence)
- [Blockchain and Crypto](#blockchain-and-crypto)
- [Data Science and Statistics](#data-science-and-statistics)
- [Cloud Computing and Distributed Systems](#cloud-computing-and-distributed-systems)
- [Ubiquitous IOT Applications and Mobile Computing](#ubiquitous-iot-applications-and-mobile-computing)
- [Educational Software and Teaching](#educational-software-and-teaching)
- [Other fun Experiments](#other-fun-experiments)

## Applied Machine Learning and Artificial Intelligence

### Real-Time Webcam Background Replacement with Neural Greenscreen 

<a href="https://github.com/PhilippMatthes/neural-greenscreen">
  <img height="200" align="center" src="https://github.com/PhilippMatthes/neural-greenscreen/raw/master/demo.png"> <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=neural-greenscreen&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

With the SARS-CoV-2 situation, video conferencing systems like Zoom became daily business. At TU Dresden, we often use BBB, which doesn't have a privacy feature to replace your background. So I wrote a plugin for my MacBook, which takes the input stream of the camera, separates the background, replaces it in real time with an image and outputs a stream to the CoreMediaIO DAL plugin interface of Mac OS. This way, I can use the plugin as a camera device for BBB and replace my background just like in Zoom. For the camera stream segmentation, the plugin uses a locally running Node.js service, which drives a pretrained BodyPix neural network via Tensorflow.js and makes the image segmentation available over a local REST interface. The camera stream is sent to this service, which returns a bitmask for where to apply background replacement. Another challenge I faced, was that this local service needs to be deployed with its own locally-signed SSL certificate, otherwise the plugin would need `NSAllowArbitraryLoads`, which potentially creates an attack surface. Additionally, energy impact was also a great challenge, which I could improve by monitoring the changes in the camera stream and updating the bitmask adaptively, depending on the user's movements.

### Detecting Objects in a Webcam Stream with YOLOCam

<a href="https://github.com/PhilippMatthes/YOLOCam">
  <img align="center" height="200" src="https://github.com/PhilippMatthes/YOLOCam/raw/master/demo.jpg"> <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=YOLOCam&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

As a learning project to the CoreMediaIO DAL interface of Mac OS, I included the YOLOv3 object detection machine learning model in a camera plugin, which shows detected objects in real-time, embedded into the camera stream. The machine learning model was included via the CoreML framework.

### 3D-ifying Photos with the 3Dify-App

<a href="https://github.com/3dify-app/ios">
  <img align="center" height="300" src="https://github.com/3dify-app/ios/raw/master/3dify-demo.gif"> <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=3dify-app&repo=ios&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

The 3Dify uses depth maps to generate immersive 3D experiences for your photos. The photo is projected onto a screen-sized plane and rendered to a 3D fragment space using a shading algorithm called parallax occlusion mapping. For this, I used the low-level iOS Metal framework instead of the deprecated OpenGL ES framework to use this shader directly on the GPU of an iPhone or iPad. To create further depth blurring effects, I used a deferred shading path with additional horizontal and vertical blur passes. The parallax occlusion mapping pass itself simply acts as if the camera is moving, when a user swipes over the screen, to create the illusion of a real occluded 3D-scene. For this, the app generates depth maps based on the disparity map (if available, only for dual/triple lense arrays) or interprets the depth information based on a machine learning model. The app is integrated with SwiftUI.

### Creating Art with Machine Learning

<a href="https://github.com/PhilippMatthes/deep-dream">
  <img align="center" height="300" src="https://github.com/PhilippMatthes/PhilippMatthes/raw/master/neural-art.jpg"> <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=deep-dream&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

For [Victoria Scheer's books Match of Survival](https://www.amazon.de/Victoria-Scheer/e/B07HKKGFS1/), I created book covers, which are stylized by neural networks, by selecting specific features of the Inception model and feeding the model output continuously back into the model. 

### Classifying NSFW Posts for My Former Instagram Bot

<a href="https://github.com/PhilippMatthes/carnivora">
  <img align="center" height="300" src="https://github.com/PhilippMatthes/carnivora/raw/master/MOCKUP.jpg?raw=true"> <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=carnivora&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Blockchain and Crypto

<a href="https://github.com/peerbridge/peerbridge">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=peerbridge&repo=peerbridge&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/peerbridge/peerbridge-ios">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=peerbridge&repo=peerbridge-ios&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/peerbridge/peerbridge-android">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=peerbridge&repo=peerbridge-android&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Data Science and Statistics

<a href="https://github.com/PhilippMatthes/PhilippMatthes">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=PhilippMatthes&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/djangostatistics">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=djangostatistics&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Cloud Computing and Distributed Systems

<a href="https://github.com/ordered-online/infrastructure">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=ordered-online&repo=infrastructure&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/peerbridge/peerbridge">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=peerbridge&repo=peerbridge&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/coffee-code-ws/entries">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=coffee-code-ws&repo=entries&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Ubiquitous IOT Applications and Mobile Computing

<a href="https://github.com/3dify-app/ios">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=3dify-app&repo=ios&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/manni-app/manni-ios">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=manni-app&repo=manni-ios&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/ordered-online/apps">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=ordered-online&repo=apps&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/pacebox-app/ios">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=pacebox-app&repo=ios&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Educational Software and Teaching

<a href="https://github.com/fragenautomat/website">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=fragenautomat&repo=website&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/coffee-code-ws/website">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=coffee-code-ws&repo=website&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/st-tu-dresden/inloop">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=st-tu-dresden&repo=inloop&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/inloop-gamified/inloop">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=inloop-gamified&repo=inloop&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

## Other fun Experiments

<a href="https://github.com/PhilippMatthes/so-many-badges">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=so-many-badges&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/dashboard">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=dashboard&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/Gitgraph">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=Gitgraph&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/better-tudscr">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=better-tudscr&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/probemon-telegram">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=probemon-telegram&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/jsExam/jsExam">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=jsExam&repo=jsExam&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/here-be-dragons">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=here-be-dragons&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>
<a href="https://github.com/PhilippMatthes/halite-java">
  <img align="center" src="https://github-readme-stats.philippmatthes.vercel.app/api/pin/?username=PhilippMatthes&repo=halite-java&show_owner=true&title_color=20bf6b&icon_color=20bf6b&text_color=0b0b0b&bg_color=fefefe" />
</a>

There is so much more. Check out my [homepage](https://philippmatth.es) for more information!

# How many people visit my profile? 📈

<a href="https://github.com/PhilippMatthes/PhilippMatthes">
  <kbd>
    <img align="center" src="https://snrmtths.uber.space/history/chart/?cache=no" alt="visits" />
  </kbd>
</a>

#### How does this work?

The shown image is fetched from my server, where I log the request and update the statistics accordingly. Of course, this requires some fiddling around with caching policies, asynchronous statistics generation by service workers and some more technical blah-blah. Just enjoy the views 😉
