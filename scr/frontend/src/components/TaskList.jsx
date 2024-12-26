import React, { useState, useEffect } from "react";
import axios from "axios";

function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/tasks/").then((response) => {
      setTasks(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Tasks</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.title} - {task.points} points
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
