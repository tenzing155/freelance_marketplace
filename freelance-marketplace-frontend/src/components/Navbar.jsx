import { Link } from "react-router-dom";
import "./Navbar.css"; // Import the custom CSS file

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <h1 className="navbar-logo">Freelance Marketplace</h1>
        <div className="navbar-links">
          <Link className="navbar-link" to="/">Home</Link>
          <Link className="navbar-link" to="/jobs">Jobs</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
