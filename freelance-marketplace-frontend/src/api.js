export const fetchJobs = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/jobs/");
    return res.json();
};
