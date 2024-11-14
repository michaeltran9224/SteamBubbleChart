import { Button } from "@/components/ui/button"
import { useForm } from "react-hook-form"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"


const FormSchema = z.object({
  username: z.string().min(17, {
    message: "Steam ID is 17 digits btw.",
  }),
})
 
function Home() {
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      username: "",
    },
  })
 
  function onSubmit(data: z.infer<typeof FormSchema>) {
    console.log("you submitted", data);
  }
 
  return (
    <div className="w-screen grid-cols-1 place-items-center">
        <div className="grid-rows-2">
          <h1>STEAM BUBBLE CHART</h1>
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="flex gap-2 items-stretch">
              <FormField
                control={form.control}
                name="username"
                render={({ field }) => (
                  <FormItem className="flex-auto">
                    <FormControl>
                      <Input placeholder="Enter your Steam ID" {...field}/>
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type="submit">Submit</Button>
            </form>
          </Form>
        </div>
    </div>
  )
}

export default Home
