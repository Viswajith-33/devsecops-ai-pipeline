# \# DevSecOps Pipeline with AI Security Summary

# 

# A GitHub Actions pipeline that scans code on every push and uses

# Google Gemini to turn the results into a ranked, plain-English summary.

# 

# \## What it does

# \- \*\*Bandit\*\*: static analysis of Python code (SQL injection, command injection, hardcoded secrets)

# \- \*\*Semgrep\*\*: pattern-based scanning with OWASP Top 10 rules, including the CI config itself

# \- \*\*pip-audit\*\*: checks dependencies for known CVEs, including transitive ones

# \- \*\*AI summary\*\*: sends the findings to Gemini and returns the top risks with fixes

# \- The API key is stored as a GitHub Secret, never in the code

# 

# \## Results on the demo app

# | Tool | Findings |

# |---|---|

# | Bandit | 4 issues in app.py (1 High, 1 Medium, 2 Low) |

# | Semgrep | 4 findings (command injection, 3 unpinned GitHub Actions) |

# | pip-audit | 13 unique vulnerabilities in 3 packages (requests, idna, urllib3) |

# 

# !\[AI summary](ai-summary.png)

# 

# The demo app (`app.py`) and the old `requests` version are deliberately

# vulnerable so the scanners have something to find.

# 

# \## Tech

# GitHub Actions, Python, Bandit, Semgrep, pip-audit, Gemini API

# 

# \## Next improvements

# \- Pin GitHub Actions to commit SHAs

# \- Fix the vulnerable code and show a passing pipeline

