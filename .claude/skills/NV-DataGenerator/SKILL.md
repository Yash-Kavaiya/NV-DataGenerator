```markdown
# NV-DataGenerator Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development conventions and workflows used in the NV-DataGenerator TypeScript codebase. You'll learn about file naming, import/export styles, commit message patterns, and how to write and run tests. This guide ensures consistency and helps you contribute effectively to the project.

## Coding Conventions

### File Naming
- Use **PascalCase** for file names.
  - Example: `DataGenerator.ts`, `UserModel.ts`

### Import Style
- Mixed import styles are used. Both default and named imports may appear.
  - Example:
    ```typescript
    import { generateData } from './DataGenerator';
    import UserModel from './UserModel';
    ```

### Export Style
- Prefer **named exports**.
  - Example:
    ```typescript
    // DataGenerator.ts
    export function generateData() { ... }
    export const DATA_VERSION = '1.0.0';
    ```

### Commit Messages
- Follow the **Conventional Commits** specification.
- Use the `feat` prefix for new features.
  - Example:
    ```
    feat: add support for custom data templates
    ```

## Workflows

### Adding a New Feature
**Trigger:** When implementing a new feature in the codebase  
**Command:** `/add-feature`

1. Create a new TypeScript file using PascalCase (e.g., `NewFeature.ts`).
2. Use named exports for all functions and constants.
3. Write or update tests in a corresponding `*.test.*` file.
4. Commit your changes using the `feat:` prefix and a concise description.
    - Example: `feat: implement user data anonymization`
5. Open a pull request for review.

### Writing Tests
**Trigger:** When adding or updating code that requires testing  
**Command:** `/write-test`

1. Create or update a test file matching the pattern `*.test.*` (e.g., `DataGenerator.test.ts`).
2. Write test cases for each exported function or feature.
3. Ensure all tests pass before committing.

## Testing Patterns

- Test files follow the `*.test.*` pattern (e.g., `DataGenerator.test.ts`).
- The specific testing framework is unknown, but standard TypeScript test patterns apply.
- Example test file structure:
    ```typescript
    import { generateData } from './DataGenerator';

    describe('generateData', () => {
      it('should generate valid data', () => {
        const data = generateData();
        expect(data).toBeDefined();
      });
    });
    ```

## Commands
| Command        | Purpose                                      |
|----------------|----------------------------------------------|
| /add-feature   | Start the workflow for adding a new feature  |
| /write-test    | Begin writing or updating test cases         |
```
