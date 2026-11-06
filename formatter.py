def format_header(cv):
    """Return the top line of the CV."""
    return f"{cv['name']} | {cv['title']} | {cv['city']}"


def format_job(job):
    """Return one line describing a job."""
    return f"{job['title']} at {job['company']} ({job['start']}-{job['end']})"


def format_cv(cv):
    """Return the whole CV as plain text."""
    lines = [format_header(cv), "", "SKILLS", ", ".join(cv["skills"]), "", "EXPERIENCE"]
    for job in cv["jobs"]:
        lines.append(format_job(job))
    return "\n".join(lines)