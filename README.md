# TopicFinder
zoom transcription

The purpose of this application is to search a professor's recorded online lecture video in order to find specified sections
that discuss a desired topic. For example, if the user is searching for "memory partitioning", the video will be searched
to find when these keywords are mentioned, and timestamps will be generated to allow the user to skip directly to the
portions of the lecture that mention "memory partitioning".

In order to accomplish this, the application will either generate a transcript for or use an existing transcript from the
video that a user selects. This transcript will then be searched to find any matches with the user-inputted keywords, and
whenever a match is found, its timestamp will be recorded so that it can be displayed to the user.

The flow of the program will look something like this:
1. The user chooses either to log in to their educational website (D2L in our case) or browse their computer for a video
   file.
2. If the user chooses to login, the application will open an instance of their default web browser to the login page of
   their educational website. From there, the user should find a video of their choosing and copy the video link back into
   the application. (Go to step 4)
3. If the user chooses to browse for a video file, the application will open an instance of the user's file manager in
   order to find and select their desired video file.
4. The application will now generate a video transcript if one is not available, or it will scan a provided transcript. In
   both cases, the application will request that the user enter a keyword (or keywords) for which they are trying to find.
5. Using the video transcript and the user's input, the application will check to find any matches between the transcript
   and user's keywords; any time a match is found, the application will record the timestamp of the match so that the user
   can then go to the exact spot in the video at which their desired topic is discussed.
