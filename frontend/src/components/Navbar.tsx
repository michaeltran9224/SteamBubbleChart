import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Link } from "react-router-dom";
import { FormSchema } from "@/pages/Home/Home";

export default function Navbar() {
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      username: "",
    },
  });

  function onSubmit(data: z.infer<typeof FormSchema>) {
    console.log("you submitted", data);
    /* TODO: Submit to backend flask and retrieve data, redirect to profile page with input. */
  }

  return (
    <nav className="fixed top-0 left-0 w-full flex items-center justify-between px-6 py-3 bg-zinc-800 shadow-sm">
      <Button variant="ghost" size="icon" className="p-0">
        <Link to="/">
          <img src="images/steam-logo-black-transparent.png" alt="Steam Logo" />
        </Link>
      </Button>

      <NavigationMenu>
        <NavigationMenuList>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Different Pages?</NavigationMenuTrigger>
            <NavigationMenuContent>
              <Link to="/">
                <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                  Michael
                </NavigationMenuLink>
              </Link>
              <Link to="/">
                <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                  Sarah
                </NavigationMenuLink>
              </Link>
            </NavigationMenuContent>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>

      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="flex flex-row gap-2"
        >
          <FormField
            control={form.control}
            name="username"
            render={({ field }) => (
              <FormItem>
                <FormControl>
                  <Input placeholder="Steam ID" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button variant="ghost" className="justify-end" type="submit">
            Submit
          </Button>
        </form>
      </Form>
    </nav>
  );
}
