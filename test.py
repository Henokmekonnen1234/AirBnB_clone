#!/usr/bin/python3
import cmd

class MyCmd(cmd.Cmd):
    intro = "Custom Command Interpreter"
    prompt = "(cmd) "

    def do_add_user(self, args):
        """Add a new user"""
        # Your logic for adding a user here
        print("User added!")

    def do_list_users(self, args):
        """List all users"""
        # Your logic for listing users here
        print("Listing all users")

    def do_quit(self, args):
        """Exit the interpreter"""
        return True

    def default(self, line):
        """Fallback for unrecognized commands"""
        if line == "User.all()":
            self.do_add_user("")
        else:
            print(f"Unknown command: {line}")

if __name__ == '__main__':
    MyCmd().cmdloop()
