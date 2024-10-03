# GPA Calculator

This is a simple GPA calculator built using Streamlit. It allows users to add grading criteria with corresponding weights, enter obtained and total marks, and calculate their GPA.

## Features

- Add custom grading criteria with weights.
- Enter obtained and total marks for each criterion.
- Automatically calculates GPA based on entered data.
- Displays the GPA and corresponding grade.

## Criteria

The GPA is calculated based on the following weights assigned to different ranges of percentages:

- **86% and above**: GPA 4.00, Grade A
- **82% - 85.99%**: GPA 3.67, Grade A-
- **78% - 81.99%**: GPA 3.33, Grade B+
- **74% - 77.99%**: GPA 3.00, Grade B
- **70% - 73.99%**: GPA 2.67, Grade B-
- **66% - 69.99%**: GPA 2.33, Grade C+
- **62% - 65.99%**: GPA 2.00, Grade C
- **58% - 61.99%**: GPA 1.67, Grade C-
- **54% - 57.99%**: GPA 1.33, Grade D+
- **50% - 53.99%**: GPA 1.00, Grade D
- **Below 50%**: GPA 0.00, Grade F

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gpa-calculator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gpa-calculator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the GPA Calculator:

1. **Add Criteria**: Define the assessment criteria (e.g., Quizzes, Projects, Exams) and assign each criterion a weight (in percentage). The total weight must sum to 100%.
2. **Enter Marks**: After adding the criteria, enter the obtained marks and the total marks for each criterion.
3. **Calculate GPA**: Once all the criteria and marks are entered, the GPA will be calculated based on the weighted average.

To run the application with Streamlit:

```bash
streamlit run app.py
```

## Example Workflow
1. Launch the app and choose "Add Criteria."
2. Define a new criterion (e.g., Quizzes) and assign a weight (e.g., 20%).
3. Add more criteria until the total weight reaches 100%.
4. Switch to "Calculate GPA" and input obtained and total marks for each criterion.
5. Click "Calculate GPA" to see your GPA and grade.