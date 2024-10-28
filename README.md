### How do you write programs that are maintainable, readable, and adaptable?

Writing maintainable, readable, and adaptable programs involves following best coding practices such as modular design, meaningful naming conventions, comprehensive documentation, and effective use of design patterns. In Project One, I applied these principles to the CRUD Python module, which was later integrated with the dashboard in Project Two. Here’s how these practices were implemented:

- **Modular Design**: I separated the CRUD operations (Create, Read, Update, Delete) into individual methods within the class. This modularity ensured that changes to one function did not affect the others, making the code easier to maintain and update.

- **Code Reusability**: The CRUD module was designed to accept various input parameters, allowing for flexible and reusable code. This design made it straightforward to adapt the module for different use cases, such as integrating it with the dashboard for dynamic data retrieval.

- **Documentation and Comments**: I used docstrings and in-line comments to provide clear explanations of each function's purpose and any complex logic. This documentation improved code readability and maintainability, making it easier for future developers to understand the codebase.

**Advantages of Working in This Way**:
- **Easier Debugging**: The modular approach allowed for independent testing of each function, simplifying the debugging process.
- **Flexible Integration**: The design facilitated the seamless integration of the CRUD operations with the dashboard widgets, enabling dynamic data updates.
- **Future Adaptability**: The CRUD module could be reused in other projects requiring database interactions, potentially being extended to work with different database systems.

---

### How do you approach a problem as a computer scientist?

As a computer scientist, I approach problems by breaking them down into smaller, manageable tasks and solving them incrementally. For this project, I began with understanding the database requirements and building a solid foundation before moving on to the dashboard:

1. **Database Setup**: I first set up the MongoDB database, ensuring that the data was correctly imported and structured. This provided a reliable foundation for the rest of the project.

2. **CRUD Module Development**: I developed the CRUD operations to meet the needs of the dashboard, which required dynamic data filtering and updates.

3. **Dashboard Development**: Using the Dash framework, I built an interactive dashboard that responded to user interactions with filters and charts.

This approach differed from previous assignments because it involved integrating multiple components (database, backend, and frontend) to create a cohesive user experience. In future projects, I will continue using modular design principles to create scalable and adaptable solutions.

---

### What do computer scientists do, and why does it matter?

Computer scientists solve problems by developing software solutions that automate processes, analyze data, and improve decision-making. In this project, my work helped Grazioso Salvare identify suitable rescue dogs by building a tool that integrates data filtering, visualization, and mapping.

By creating an interactive dashboard, I enabled the company to analyze data efficiently, make informed decisions, and streamline the process of selecting dogs for training. This type of solution saves time, enhances decision accuracy, and supports the organization in achieving its mission.

Overall, computer scientists play a crucial role in driving innovation, increasing productivity, and enabling organizations to leverage data for better decision-making.
