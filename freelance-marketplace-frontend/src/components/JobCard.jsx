import { Link } from "react-router-dom";

const JobCard = ({ job }) => {
  return (
    <div className="border p-4 rounded-lg shadow-md hover:shadow-lg transition">
      <h2 className="text-xl font-bold">{job.title}</h2>
      <p className="text-gray-600">{job.description}</p>
      <p className="text-green-600 font-semibold">${job.budget}</p>
      <Link className="text-blue-500 hover:underline mt-2 inline-block" to={`/jobs/${job.id}`}>
        View Details
      </Link>
    </div>
  );
};

export default JobCard;
