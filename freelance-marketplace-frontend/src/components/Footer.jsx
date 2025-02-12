import React from "react";
import "./Footer.css"; // Import the CSS for the footer

const Footer = () => {
  return (
    <footer className="footer">
      <p>
        &copy; {new Date().getFullYear()} Freelance Marketplace. All rights reserved.
      </p>
      <p>
        Designed by <a href="https://your-website.com" target="_blank" rel="noopener noreferrer">Your Name</a>
      </p>
    </footer>
  );
};

export default Footer;
