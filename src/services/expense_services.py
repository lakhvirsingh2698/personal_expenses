from src.database.db_connections import connect_db, close_db


def add_expense(expense):
    conn = connect_db()
    if not conn:
        print("Database connection failed. Expense not added.")
        return

    cursor = None

    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO expenses (title, amount, category, expense_date)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            expense.title,
            expense.amount,
            expense.category,
            expense.expense_date
        )

        cursor.execute(query, values)
        conn.commit()
        print("Expense added successfully!")

    except Exception as e:
        print(f"Error adding expense: {e}")

    finally:
        if cursor:
            cursor.close()
        close_db(conn)


def view_expenses():
    conn = connect_db()
    if not conn:
        print("Database connection failed. Cannot fetch expenses.")
        return

    cursor = None

    try:
        cursor = conn.cursor()
        query = """
        SELECT id, title, amount, category, expense_date, created_at
        FROM expenses
        ORDER BY expense_date DESC, id DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No expenses found.")
            return

        # Convert rows into list of dictionaries (Phase 1 improvement)
        expenses = [
            {
                "id": row[0],
                "title": row[1],
                "amount": float(row[2]),
                "category": row[3],
                "expense_date": str(row[4]),
                "created_at": str(row[5])
            }
            for row in rows
        ]

        print("\n==================== ALL EXPENSES ====================")
        print(f"{'ID':<5} {'Title':<20} {'Amount':<12} {'Category':<15} {'Date':<12}")
        print("-" * 70)

        for expense in expenses:
            print(
                f"{expense['id']:<5} "
                f"{expense['title']:<20} "
                f"{expense['amount']:<12.2f} "
                f"{expense['category']:<15} "
                f"{expense['expense_date']:<12}"
            )

        print("-" * 70)
        print(f"Total records: {len(expenses)}")

    except Exception as e:
        print(f"Error fetching expenses: {e}")

    finally:
        if cursor:
            cursor.close()
        close_db(conn)


def update_expense(expense_id, expense):
    conn = connect_db()
    if not conn:
        print("Database connection failed. Expense not updated.")
        return

    cursor = None

    try:
        cursor = conn.cursor()
        query = """
        UPDATE expenses
        SET title = %s, amount = %s, category = %s, expense_date = %s
        WHERE id = %s
        """
        values = (
            expense.title,
            expense.amount,
            expense.category,
            expense.expense_date,
            expense_id
        )

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("Expense updated successfully!")
        else:
            print("Expense not found.")

    except Exception as e:
        print(f"Error updating expense: {e}")

    finally:
        if cursor:
            cursor.close()
        close_db(conn)


def delete_expense(expense_id):
    conn = connect_db()
    if not conn:
        print("Database connection failed. Expense not deleted.")
        return

    cursor = None

    try:
        cursor = conn.cursor()
        query = "DELETE FROM expenses WHERE id = %s"
        cursor.execute(query, (expense_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    except Exception as e:
        print(f"Error deleting expense: {e}")

    finally:
        if cursor:
            cursor.close()
        close_db(conn)