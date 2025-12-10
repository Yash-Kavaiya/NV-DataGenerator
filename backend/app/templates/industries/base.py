"""Base industry template with common terminology and prompts."""

from dataclasses import dataclass, field


@dataclass
class IndustryTemplate:
    """Template for industry-specific transcript generation."""
    
    id: str
    name: str
    
    # Domain vocabulary
    terminology: list[str] = field(default_factory=list)
    
    # Common agent phrases
    agent_greetings: list[str] = field(default_factory=list)
    agent_closings: list[str] = field(default_factory=list)
    hold_phrases: list[str] = field(default_factory=list)
    
    # Compliance/required phrases
    compliance_phrases: list[str] = field(default_factory=list)
    
    # Scenario-specific context
    scenario_context: dict[str, str] = field(default_factory=dict)
    
    # Products/services mentioned
    products_services: list[str] = field(default_factory=list)
    
    # Departments for transfers
    departments: list[str] = field(default_factory=list)

    def get_prompt_context(self, scenario: str) -> str:
        """Generate industry-specific context for the LLM prompt."""
        context_parts = [
            f"Industry: {self.name}",
            f"\nDomain Terminology to use naturally: {', '.join(self.terminology[:10])}",
            f"\nProducts/Services: {', '.join(self.products_services[:5])}",
            f"\nDepartments: {', '.join(self.departments)}",
        ]
        
        if scenario in self.scenario_context:
            context_parts.append(f"\nScenario Context: {self.scenario_context[scenario]}")
        
        if self.compliance_phrases:
            context_parts.append(f"\nCompliance phrases to include when appropriate: {self.compliance_phrases[0]}")
        
        return "\n".join(context_parts)

    def get_agent_greeting(self) -> str:
        if self.agent_greetings:
            return self.agent_greetings[0]
        return "Thank you for calling. How may I assist you today?"

    def get_agent_closing(self) -> str:
        if self.agent_closings:
            return self.agent_closings[0]
        return "Is there anything else I can help you with today?"
