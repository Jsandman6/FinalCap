def risk_assessment_questionnaire():
  """
  Asks the user a series of questions to assess their risk tolerance.

  Returns:
    A string representing the user's risk profile.
  """

  # Define the list of questions
  questions = [
    "What is your investment objective?",
    "What is your investment horizon?",
    "What is your tax situation?",
    "What are your investment knowledge and experience?",
  ]

  # Get user input for each question
  answers = []
  for question in questions:
    answer = input(question + "\n")
    answers.append(answer)

  # Print the risk profile based on the answers
  risk_profile = ""
  if answers[1] == "low":
    risk_profile = "conservative"
  elif answers[1] == "medium":
    risk_profile = "moderate"
  else:
    risk_profile = "aggressive"

  print("\nYour risk profile is:", risk_profile)

  return risk_profile

# Call the function
risk_profile = risk_assessment_questionnaire()

if __name__ == '__main__' :
 print("\nYour risk profile is:", risk_profile)