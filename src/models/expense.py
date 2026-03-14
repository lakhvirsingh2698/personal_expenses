class Expense:
    def __init__(self, title, amount, category, expense_date, expense_id=None):
        self.id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.expense_date = expense_date

    def to_dict(self):
        """
        Convert Expense object into dictionary format.
        Useful for printing, exporting, and future JSON support.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "expense_date": self.expense_date
        }

    def __str__(self):
        return (
            f"Expense(id={self.id}, title='{self.title}', amount={self.amount}, "
            f"category='{self.category}', expense_date='{self.expense_date}')"
        )