import React from "react";
import "./Home.css";

const Home = ({ message, responseData }) => {
  return (
    <div className="home-container">
      <h1 className="home-title">{message}</h1>
      <p className="home-message">Welcome to our marketplace! Explore the amazing items below.</p>
      <div className="home-items-list">
        {responseData.map((item) => (
          <div key={item.id} className="home-item">
            <h3>{item.title}</h3>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
