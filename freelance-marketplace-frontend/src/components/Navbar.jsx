import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4 text-white flex justify-between items-center">
      <h1 className="text-2xl font-bold">Freelance Marketplace</h1>
      <div>
        <Link className="mx-2 hover:underline" to="/">Home</Link>
        <Link className="mx-2 hover:underline" to="/jobs">Jobs</Link>
      </div>
    </nav>
  );
};

export default Navbar;
