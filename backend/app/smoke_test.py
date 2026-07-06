from crewai import Agent, Task, Crew, LLM

print("=" * 70)
print("Smoke Test: CrewAI + Ollama + qwen2.5:7b")
print("=" * 70)

llm = LLM(
    model="ollama/qwen2.5:7b",
    base_url="http://localhost:11434",
)

agent = Agent(
    role="Test Agent",
    goal="Verify CrewAI can communicate with the local Ollama server.",
    backstory="A minimal agent used only to validate the development environment.",
    llm=llm,
    verbose=True,
)

task = Task(
    description=(
        "Reply with exactly this sentence and nothing else:\n"
        "CrewAI is connected to Ollama."
    ),
    expected_output="CrewAI is connected to Ollama.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
)

print("\nRunning CrewAI smoke test...\n")

result = crew.kickoff()

print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)
print(result)
print("=" * 70)