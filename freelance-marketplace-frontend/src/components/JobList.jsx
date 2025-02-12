import { useEffect, useState } from "react";
import axios from "axios";
import JobCard from "./JobCard";

const JobList = () => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/jobs/")
      .then((response) => {
        setJobs(response.data);
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
      });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Available Jobs</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {jobs.length > 0 ? jobs.map((job) => (
          <JobCard key={job.id} job={job} />
        )) : (
          <p>No jobs found.</p>
        )}
      </div>
    </div>
  );
};

export default JobList;
