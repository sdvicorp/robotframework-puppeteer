The way I got this working was...

setup a virtualenv:

  - go to parent folder so as not to pollute this repo.
  - `virtualenv venv`
  - `source venv/bin/activate`

Then in this folder:

  - `pip3 install -r requirements.txt`

Setup is complete!  Now to run the POC:

  - Get Access ready for the test: go into Access, go to settings.  Change the ARL to something bogus, and save it.
  - Close the Access panel and reopen it.  With the above change it should halt on the ARL form at the very beginning of the app.
  - in this folder, run `(export PYTHONPATH=$(pwd) ; cd Examples/cep-plugin ; robot submit-arl.robot )`

If anything goes wrong, run!
