#!/usr/bin/python3
""" main program executable """

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    prompt = '(hbnb) '
    cls_list = ["BaseModel", "User"]

    def emptyline(self):
        """ override emptyline func """
        pass

    def do_quit(self, arg):
        """ Close """
        return True

    def do_EOF(self, arg):
        """ close """
        return True

    def help_EOF(self):
        """ eof help """
        print("Quit command to exit program:\n")

    def do_create(self, arg):
        """creates a new instance"""
        args = arg.split()
        if not len(args):
            print("** class name missing **")
        else:
            dic = {"BaseModel": BaseModel, "User": User}
            if args[0] in dic.keys():
                new = dic[args[0]]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """"Prints the string representation of an instance """
        args = arg.split()
        if not len(args):
            print("** class name missing **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                name = args[0] + "." + args[1]
                all_objs = storage.all()
                if name in all_objs:
                    print(all_objs[name])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        args = arg.split()
        if not len(args):
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.cls_list:
            print("** class doesn't exist **")
        else:
            name = args[0] + "." + args[1]
            all_objs = storage.all()
            if name not in all_objs:
                print("** no instance found **")
            else:
                all_objs.pop(name)
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = storage.all()
        if len(args) and args[0] not in self.cls_list or not all_objs:
            print("** class doesn't exist **")
        elif len(args) and args[0] in self.cls_list:
            list_n = [str(v) for k, v in all_objs.items()
                      if k.split(".")[0] == args[0]]
            print(list_n)
        else:
            list_n = [str(v) for v in all_objs.values()]
            print(list_n)

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        args = arg.split()
        all_objs = storage.all()
        status = 0

        for i in range(4):
            try:
                args[i]
            except:
                if status == 0:
                    print("** class name missing **")
                elif status == 1:
                    print("** instance id missing **")
                elif status == 2:
                    print("** attribute name missing **")
                else:
                    print("** value missing **")
                break
            if i == 0:
                if args[i] not in self.cls_list:
                    print("** class doesn't exist **")
                    break
            elif i == 1:
                name = args[0] + "." + args[1]
                if name not in all_objs.keys():
                    print("** no instance found **")
                    break
            elif i == 2:
                pass
            else:
                attr = ["id", "create_at", "updated_at"]
                if args[2] not in attr:
                    if hasattr(all_objs[name], args[2]):
                        get_type = type(getattr(all_objs[name], args[2]))
                        try:
                            args[3] = get_type(args[3])
                            args[3] = args[3].strip('"')
                            setattr(all_objs[name], args[2],
                                    get_type(args[3].strip('"')))
                            storage.save()
                        except:
                            pass
                    else:
                        args[3] = args[3].strip('"')
                        setattr(all_objs[name], args[2], args[3].strip('"'))
                        storage.save()

            if i < 3:
                status += 1

if __name__ == '__main__':
    HBNBCommand().cmdloop()
