from agents.planner_agent import route_query

query = input("Ask something: ")

agent = route_query(query)

print("\nSelected Agent:")
print(agent)