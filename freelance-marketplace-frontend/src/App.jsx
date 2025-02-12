import { Route, Routes } from "react-router-dom";  // Import routing components
import { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "./components/Navbar";  // Import Navbar
import Footer from "./components/Footer";  // Import Footer
import Home from "./pages/Home";  // Assuming you have a Home page component
import Jobs from "./pages/Jobs";  // Assuming you have a Jobs page component

function App() {
  const [message, setMessage] = useState("");  // State for welcome message
  const [responseData, setResponseData] = useState([]);  // State for home items
  const [jobs, setJobs] = useState([]);  // State for job listings

  // Fetch home data
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/home/")
      .then((response) => {
        console.log("API response for home:", response.data);
        setMessage(response.data.message);  // Set the home message
        setResponseData(response.data.items || []);  // Set the home items list
      })
      .catch((error) => {
        console.error("Error fetching home data:", error);
      });
  }, []);

  // Fetch job listings data
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/jobs/")
      .then((response) => {
        console.log("API response for jobs:", response.data);
        setJobs(response.data);  // Set the jobs list
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
      });
  }, []);  // This effect runs once when the component mounts

  return (
    <div id="root">
      <Navbar />  {/* Include Navbar at the top of the page */}
      <div className="main-content">
      <Routes>
        <Route path="/" element={<Home message={message} responseData={responseData} />} />
        <Route path="/jobs" element={<Jobs jobs={jobs} />} />
      </Routes>
      </div>
      <Footer />  {/* Include Footer at the bottom of the page */}
    </div>
  );
}

export default App;
