import React, { useState } from "react";
import axios from "axios";

function AddTask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const addTask = () => {
    axios
      .post("http://localhost:8000/tasks/", { title, description })
      .then(() => {
        setTitle("");
        setDescription("");
      });
  };

  return (
    <div>
      <h2>Add Task</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={addTask}>Add</button>
    </div>
  );
}

export default AddTask;

