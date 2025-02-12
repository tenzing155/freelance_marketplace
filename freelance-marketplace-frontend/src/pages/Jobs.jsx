import React from "react";
import "./Jobs.css";

const Jobs = ({ jobs }) => {
  return (
    <div className="jobs-container">
      <h1 className="jobs-title">Available Jobs</h1>
      <div className="jobs-list">
        {jobs.map((job) => (
          <div key={job.id} className="job-item">
            <h3>{job.title}</h3>
            <p>{job.description}</p>
            <p className="job-budget">Budget: ${job.budget}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Jobs;
