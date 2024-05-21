<center> <h1>AirBnB clone - The console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>


| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/MarkBrendan/AirBnB_clone/blob/main/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/MarkBrendan/AirBnB_clone/) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/MarkBrendan/AirBnB_clone/) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/MarkBrendan/AirBnB_clone/) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/_ _init_ _.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/base_model.py](https://github.com/MarkBrendan/AirBnB_clone/) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/MarkBrendan/AirBnB_clone/) | Add basic functionality to console program, allowing it to quit, handle empty lines and EOF |
| 7. Console 0.1 | [console.py](https://github.com/MarkBrendan/AirBnB_clone/) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/engine/file_storage.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/user.py](https://github.com/MarkBrendan/AirBnB_clone/) | Dynamically implements a user class ]
| 9. More Classes | [/models/user.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/place.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/city.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/amenity.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/state.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/review.py](https://github.com/MarkBrendan/AirBnB_clone/) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/MarkBrendan/AirBnB_clone/) [/models/engine/file_storage.py](https://github.com/MarkBrendan/AirBnB_clone/) | Update the console and file storage system to work dynamically with all classes update file storage |
<br>
